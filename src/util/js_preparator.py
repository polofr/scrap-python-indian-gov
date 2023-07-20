from src.config.states_simplified import STATES_SIMPLIFIED


class JsPreparator:
    @staticmethod
    def get_state_code(state_name):
        state_code = STATES_SIMPLIFIED.get(state_name)
        if not state_code:
            raise Exception(f"{state_name} is not a correct state name")
        return state_code

    @staticmethod
    def prepare_state(financial_year, financial_year_plan, state_name):
        state_name = state_name.upper()
        state_code = JsPreparator.get_state_code(state_name)

        script = f"""
fnyearId="{financial_year}"
planyearid="{financial_year_plan}"
$("#levelId").val(0);
level=3
$("#accordionflgId").val(level);
document.getElementById("planyearid").value=planyearid;
state_cd='{state_code}'
statenm='{state_name}'
$("#levelId").val(level);
$("#fnyearId").val(fnyearId);
$("#stateId").val(state_cd);
$("#statenmId").val(statenm);
        """
        return script

    @staticmethod
    def get_list_of_districts(financial_year, state_name):
        state_name = state_name.upper()
        state_code = STATES_SIMPLIFIED.get(state_name)
        if not state_code:
            raise Exception(f"{state_name} is not a correct state name")
        return f"""
getreport('{state_code}', 3, '{financial_year}', '{state_name}');
        """

    @staticmethod
    def get_list_of_panchayats(
        financial_year, state_name, district_code, block_panch_code
    ):
        state_name = state_name.upper()
        state_code = STATES_SIMPLIFIED.get(state_name)
        if not state_code:
            raise Exception(f"{state_name} is not a correct state name")
        return f"""
getgpreport('{state_code}',3,'{financial_year}','{district_code}','{block_panch_code}',0);
        """

    @staticmethod
    def get_list_of_panchayat_report(
        financial_year, financial_year_plan, state_name, district_code, block_panch_code
    ):
        state_code = JsPreparator.get_state_code(state_name)
        script = JsPreparator.prepare_state(
            financial_year=financial_year,
            financial_year_plan=financial_year_plan,
            state_name=state_name,
        )
        script += """
        function getgpreportBis(state_cd,level,fyear,zp_cd,bp_cd,typcod){
             $("#levelId").val(level);
             $("#stateId").val(state_cd);
             $("#fnyearId").val(fyear);
             $("#zpcdId").val(zp_cd);
             $("#bpcdId").val(bp_cd);
             $("#local_body_typ_cdid").val(typcod);
             $("#accordionflgId").val(3);
        }
        """
        script += f"""
            getgpreportBis('{state_code}',3,'{financial_year}','{district_code}','{block_panch_code}',0);
            """
        return script
