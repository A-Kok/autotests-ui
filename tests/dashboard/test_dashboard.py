from pages.dashboard.dashboard_page import DashboardPage
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.navigate(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_student_chart()
        dashboard_page_with_state.check_visible_activities_chart()