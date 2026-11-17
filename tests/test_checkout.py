from playwright.sync_api import expect


def apply_code(page, code):
    page.get_by_label("Discount code").fill(code)
    page.get_by_role("button", name="Apply code").click()


def test_ck01_initial_order_summary(checkout):
    expect(checkout.get_by_role("heading", name="Checkout")).to_be_visible()
    expect(checkout.locator("#discount")).to_have_text("$0.00")
    expect(checkout.locator("#total")).to_have_text("$55.00")


def test_ck02_valid_code_updates_displayed_total(checkout):
    apply_code(checkout, "SAVE10")
    expect(checkout.locator("#promo-message")).to_have_text("SAVE10 applied.")
    expect(checkout.locator("#discount")).to_have_text("$5.00")
    expect(checkout.locator("#total")).to_have_text("$50.00", timeout=1000)


def test_ck03_code_ignores_case_and_whitespace(checkout):
    apply_code(checkout, "  save10  ")
    expect(checkout.locator("#promo-message")).to_have_text("SAVE10 applied.", timeout=1000)
    expect(checkout.locator("#discount")).to_have_text("$5.00")


def test_ck04_unknown_code_preserves_original_total(checkout):
    apply_code(checkout, "EXPIRED")
    expect(checkout.locator("#promo-message")).to_have_text("Code not recognized.")
    expect(checkout.locator("#discount")).to_have_text("$0.00")
    expect(checkout.locator("#total")).to_have_text("$55.00")


def test_ck05_reapplying_code_does_not_stack_discount(checkout):
    apply_code(checkout, "SAVE10")
    apply_code(checkout, "SAVE10")
    expect(checkout.locator("#discount")).to_have_text("$5.00")
    checkout.get_by_role("button", name="Place demo order").click()
    expect(checkout.locator("#confirmation")).to_have_text("Order FS-0001 confirmed · $50.00")


def test_ck06_first_order_has_reference_and_amount(checkout):
    checkout.get_by_role("button", name="Place demo order").click()
    expect(checkout.locator("#confirmation")).to_have_text("Order FS-0001 confirmed · $55.00")


def test_ck07_confirmation_prevents_second_order(checkout):
    place = checkout.get_by_role("button", name="Place demo order")
    place.click()
    expect(checkout.locator("#confirmation")).to_contain_text("FS-0001")
    expect(place).to_be_disabled(timeout=1000)


def test_ck08_unknown_code_preserves_an_applied_discount(checkout):
    apply_code(checkout, "SAVE10")
    apply_code(checkout, "EXPIRED")
    expect(checkout.locator("#promo-message")).to_have_text(
        "Code not recognized. SAVE10 is still applied."
    )
    expect(checkout.locator("#discount")).to_have_text("$5.00")
