from src.util.js_preparator import JsPreparator


def test_prepare_state():
    res = JsPreparator.prepare_state(
        financial_year="2020", financial_year_plan="2020-2021", state_name="MAHARASHTRA"
    )
    print(res)
