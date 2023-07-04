# Generated by Django 4.1.7 on 2023-04-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PDIModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("PDI_ID", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_CD_PROCESS",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                (
                    "PDI_CD_COMPANY",
                    models.CharField(blank=True, max_length=4, null=True),
                ),
                ("PDI_CD_PLANT", models.CharField(blank=True, max_length=4, null=True)),
                ("PDI_ID_SCHD", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "PDI_CD_STATUS",
                    models.CharField(blank=True, max_length=2, null=True),
                ),
                ("PDI_ID_INPUT_COIL", models.CharField(max_length=10)),
                ("PDI_INP_SEC1_COIL", models.FloatField(blank=True, null=True)),
                ("PDI_INP_SEC2_COIL", models.FloatField(blank=True, null=True)),
                ("PDI_INP_LN_COIL", models.IntegerField(blank=True, null=True)),
                ("PDI_INP_MS_COIL", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_INP_FL_SLEEVE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_INP_IDIA_COIL", models.IntegerField(blank=True, null=True)),
                ("PDI_INP_ODIA_COIL", models.IntegerField(blank=True, null=True)),
                ("PDI_SOURCE", models.CharField(blank=True, max_length=1, null=True)),
                (
                    "PDI_INP_FL_TRIM",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_FL_TRIM", models.CharField(blank=True, max_length=1, null=True)),
                ("PDI_AIM_SEC2_AFT_TRIM", models.FloatField(blank=True, null=True)),
                ("PDI_IDIA", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_FL_SLEEVE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_CD_PROD", models.CharField(blank=True, max_length=3, null=True)),
                ("PDI_CD_QLTY", models.CharField(blank=True, max_length=6, null=True)),
                ("PDI_TDC_NO", models.CharField(blank=True, max_length=5, null=True)),
                ("PDI_NO_SEQ", models.IntegerField(blank=True, null=True)),
                ("PDI_INP_EFF_IDIA_COIL", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_INP_PROD_CD",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                (
                    "PDI_INP_QLTY_CD",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
                (
                    "PDI_INP_TDC_NO",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "PDI_CD_PREV_PROC",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                ("PDI_HD_TGT_OFF_GUAGE", models.IntegerField(blank=True, null=True)),
                ("PDI_TL_TGT_OFF_GUAGE", models.IntegerField(blank=True, null=True)),
                ("PDI_OFF_GUAGE_HD", models.IntegerField(blank=True, null=True)),
                ("PDI_OFF_GUAGE_TL", models.IntegerField(blank=True, null=True)),
                ("PDI_ROLL_UP_HD", models.IntegerField(blank=True, null=True)),
                ("PDI_ROLL_UP_TL", models.IntegerField(blank=True, null=True)),
                ("PDI_NO_WELD", models.IntegerField(blank=True, null=True)),
                ("PDI_WELD_LOCN1", models.IntegerField(blank=True, null=True)),
                ("PDI_WELD_LOCN2", models.IntegerField(blank=True, null=True)),
                ("PDI_WELD_LOCN3", models.IntegerField(blank=True, null=True)),
                ("PDI_WELD_LOCN4", models.IntegerField(blank=True, null=True)),
                ("PDI_MIN_SEC2_AFT_TRIM", models.FloatField(blank=True, null=True)),
                ("PDI_MAX_SEC2_AFT_TRIM", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_PROC_CODE",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                ("PDI_REPROC_CNTR", models.IntegerField(blank=True, null=True)),
                ("PDI_HD_NO_SMPL", models.IntegerField(blank=True, null=True)),
                ("PDI_M1_NO_SMPL", models.IntegerField(blank=True, null=True)),
                ("PDI_M2_NO_SMPL", models.IntegerField(blank=True, null=True)),
                ("PDI_TL_NO_SMPL", models.IntegerField(blank=True, null=True)),
                ("PDI_FL_INSP", models.CharField(blank=True, max_length=1, null=True)),
                (
                    "PDI_INSP_TYPE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_ID_ORDER",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("PDI_ID_ORDER_ITEM", models.IntegerField(blank=True, null=True)),
                ("PDI_ID_ORDER_PART", models.IntegerField(blank=True, null=True)),
                ("PDI_YR_WK_DISP", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_CUSTOMER_DESC",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "PDI_SHIP_TO_PARTY_CD",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
                (
                    "PDI_SHIP_CUST_DESC",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "PDI_DESTINATION",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("PDI_AIM_SEC1_ORDER", models.FloatField(blank=True, null=True)),
                ("PDI_MIN_SEC1_ORDER", models.FloatField(blank=True, null=True)),
                ("PDI_MAX_SEC1_ORDER", models.FloatField(blank=True, null=True)),
                ("PDI_AIM_SEC2_ORDER", models.FloatField(blank=True, null=True)),
                ("PDI_MIN_SEC2_ORDER", models.FloatField(blank=True, null=True)),
                ("PDI_MAX_SEC2_ORDER", models.FloatField(blank=True, null=True)),
                ("PDI_ORD_MS_COIL_MIN", models.IntegerField(blank=True, null=True)),
                ("PDI_ORD_MS_COIL_MAX", models.IntegerField(blank=True, null=True)),
                ("PDI_ORD_LN_COIL_MIN", models.IntegerField(blank=True, null=True)),
                ("PDI_ORD_LN_COIL_MAX", models.IntegerField(blank=True, null=True)),
                (
                    "PDI_ORDER_EDGE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_CD_END_USE",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("PDI_CUT_DIR", models.IntegerField(blank=True, null=True)),
                ("PDI_MS_COIL_MIN", models.IntegerField(blank=True, null=True)),
                ("PDI_MS_COIL_MAX", models.IntegerField(blank=True, null=True)),
                ("PDI_LN_COIL_MAX", models.IntegerField(blank=True, null=True)),
                ("PDI_LN_COIL_MIN", models.IntegerField(blank=True, null=True)),
                ("PDI_AIM_SEC1", models.FloatField(blank=True, null=True)),
                ("PDI_MIN_SEC1", models.FloatField(blank=True, null=True)),
                ("PDI_MAX_SEC1", models.FloatField(blank=True, null=True)),
                (
                    "PDI_WELD_IN_COIL",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_CD_NEXT_PROC",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                ("PDI_GRADE", models.CharField(blank=True, max_length=4, null=True)),
                (
                    "PDI_PROC_CHT_NO",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "PDI_SURFACE_GRADE",
                    models.CharField(blank=True, max_length=2, null=True),
                ),
                (
                    "PDI_SHAPE_GRADE",
                    models.CharField(blank=True, max_length=2, null=True),
                ),
                (
                    "PDI_FL_OILING",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_MS_OIL_COAT_MIN", models.IntegerField(blank=True, null=True)),
                ("PDI_MS_OIL_COAT_MAX", models.IntegerField(blank=True, null=True)),
                ("PDI_OIL_TYP", models.CharField(blank=True, max_length=1, null=True)),
                ("PDI_OIL_QTY", models.CharField(blank=True, max_length=1, null=True)),
                (
                    "PDI_STRAP_CODE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_LABEL", models.CharField(blank=True, max_length=1, null=True)),
                ("PDI_CD_PACK", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "PDI_CD_SEAL_PAD",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_COIL_TYPE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_SCHD_UNIT",
                    models.CharField(blank=True, max_length=3, null=True),
                ),
                ("PDI_DT_CREATE", models.DateTimeField(blank=True, null=True)),
                (
                    "PDI_SHFT_CREATE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_DT_UPDATE", models.DateTimeField(blank=True, null=True)),
                (
                    "PDI_SHFT_UPDATE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_CREATE_ID",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                (
                    "PDI_UPDATE_ID",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                ("PDI_TS_REC_CREATE", models.DateTimeField(blank=True, null=True)),
                ("PDI_TS_REC_UPDATE", models.DateTimeField(blank=True, null=True)),
                ("PDI_AGE_AT_INV", models.FloatField(blank=True, null=True)),
                ("PDI_AVLBL_HRS", models.FloatField(blank=True, null=True)),
                ("PDI_MILL_OUT_LEN", models.FloatField(blank=True, null=True)),
                ("PDI_MILL_CUM_LEN", models.FloatField(blank=True, null=True)),
                ("PDI_SEC2_AFT_SLIT_1", models.FloatField(blank=True, null=True)),
                ("PDI_SEC2_AFT_SLIT_2", models.FloatField(blank=True, null=True)),
                ("PDI_SEC2_AFT_SLIT_3", models.FloatField(blank=True, null=True)),
                ("PDI_SEC2_AFT_SLIT_4", models.FloatField(blank=True, null=True)),
                ("PDI_SEC2_AFT_SLIT_5", models.FloatField(blank=True, null=True)),
                ("PDI_LEN_AFT_SLIT_1", models.FloatField(blank=True, null=True)),
                ("PDI_LEN_AFT_SLIT_2", models.FloatField(blank=True, null=True)),
                ("PDI_LEN_AFT_SLIT_3", models.FloatField(blank=True, null=True)),
                ("PDI_LEN_AFT_SLIT_4", models.FloatField(blank=True, null=True)),
                ("PDI_LEN_AFT_SLIT_5", models.FloatField(blank=True, null=True)),
                ("PDI_CAST_NO", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "PDI_REMARKS",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("PDI_CARBON", models.FloatField(blank=True, null=True)),
                ("PDI_SILICA", models.FloatField(blank=True, null=True)),
                ("PDI_MANGANESE", models.FloatField(blank=True, null=True)),
                ("PDI_PHOSPHOROUS", models.FloatField(blank=True, null=True)),
                ("PDI_ALUMINIUM", models.FloatField(blank=True, null=True)),
                ("PDI_NITROGEN", models.FloatField(blank=True, null=True)),
                ("PDI_TITENIUM", models.FloatField(blank=True, null=True)),
                ("PDI_DEFECT_1", models.CharField(blank=True, max_length=5, null=True)),
                (
                    "PDI_DEFECT_1_DESC",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "PDI_DEFECT_SEVERITY_1",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "PDI_DEFECT_LENGTH_1",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("PDI_DEFECT_2", models.CharField(blank=True, max_length=5, null=True)),
                (
                    "PDI_DEFECT_2_DESC",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "PDI_DEFECT_SEVERITY_2",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                (
                    "DEFECT_LENGTH_2",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "PDI_YIELD_POINT_HR",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "PDI_HARDNESS_HR",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "PDI_FULL_HARD_COIL_POSITIVE_THICKNESS_TOL",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "PDI_FULL_HARD_COIL_NEGATIVE_THICKNESS_TOL",
                    models.FloatField(blank=True, null=True),
                ),
                (
                    "PDI_NEXT_LINE_PROCESS",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("PDI_HR_TDC", models.CharField(blank=True, max_length=4, null=True)),
                (
                    "PDI_HR_QUALITY",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
                ("PDI_FIN_ROLLING_TEMP", models.FloatField(blank=True, null=True)),
                ("PDI_COOLING_TEMP", models.FloatField(blank=True, null=True)),
                (
                    "PDI_CROWN_HR",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "PDI_WEDGE_HR",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "PDI_MILL_MODE",
                    models.CharField(blank=True, max_length=1, null=True),
                ),
                ("PDI_RECO_REDUCTION", models.FloatField(blank=True, null=True)),
                ("PDI_RECO_ELONGATION", models.FloatField(blank=True, null=True)),
                (
                    "PDI_OFF_GAUGE_LENGTH_HEAD_END",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "PDI_OFF_GAUGE_LENGTH_TAIL_END",
                    models.IntegerField(blank=True, null=True),
                ),
                ("PDI_SPARE1", models.CharField(blank=True, max_length=15, null=True)),
                ("PDI_SPARE2", models.CharField(blank=True, max_length=15, null=True)),
                ("PDI_SPARE3", models.CharField(blank=True, max_length=15, null=True)),
                ("PDI_SPARE4", models.CharField(blank=True, max_length=15, null=True)),
                ("PDI_SPARE5", models.CharField(blank=True, max_length=15, null=True)),
                ("PDI_SPARE6", models.IntegerField(blank=True, null=True)),
                ("PDI_SPARE7", models.IntegerField(blank=True, null=True)),
                ("PDI_SPARE8", models.IntegerField(blank=True, null=True)),
                ("PDI_SPARE9", models.IntegerField(blank=True, null=True)),
                ("PDI_SPARE10", models.IntegerField(blank=True, null=True)),
                ("PDI_READ_FLAG", models.BooleanField(default=False)),
            ],
        ),
    ]