import datetime
from io import BytesIO

from django.views import View
from django.http import HttpResponse
from openpyxl import Workbook

from .models import Robot


class RobotsInfoReportExcel(View):

    def get(self, request):
        one_week_ago = datetime.datetime.now() - datetime.timedelta(days=7)
        robots = Robot.objects.filter(created__gte=one_week_ago)

        summary_data = {}
        for robot in robots:
            if robot.model not in summary_data:
                summary_data[robot.model] = {}
            if robot.version not in summary_data[robot.model]:
                summary_data[robot.model][robot.version] = 0
            summary_data[robot.model][robot.version] += 1

        wb = Workbook()

        default_sheet = wb.active
        wb.remove(default_sheet)

        for model, versions in summary_data.items():
            ws = wb.create_sheet(title=model)
            ws.append(["Модель", "Версия", "Количество за неделю"])
            for version, count in versions.items():
                ws.append([model, version, count])

        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response["Content-Disposition"] = "attachment; filename=web_source_table.xlsx"

        with BytesIO() as buffer:
            wb.save(buffer)
            buffer.seek(0)
            response.write(buffer.getvalue())

        return response
