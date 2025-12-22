from app.schemas.ai_report import AIReportType

class DataProcessPrompts:
    def __init__(self, request_type: AIReportType):
        self.request_type = request_type

    def get_prompt(self) -> str:
        # This is a placeholder for the actual prompt generation logic.
        # You should replace this with your actual implementation.
        return f"Prompt for {self.request_type.value}"
