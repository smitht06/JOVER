from wagtail.admin.panels import FieldPanel
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import Person, Campaign, ContactLog, Materials


class CampaignViewSet(SnippetViewSet):
    model = Campaign
    icon = "crosshairs"
    menu_label = "Campaigns"
    menu_name = "Campaigns"
    menu_order = 300
    add_to_admin_menu = True
    list_display = ["name", "candidate", "election_date", "office", "district", UpdatedAtColumn()]


register_snippet(CampaignViewSet)
