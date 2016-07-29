from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from poll.models import PollPluginModel
from django.utils.translation import ugettext as _


class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel
    module = _("Polls")
    name = _("Poll Plugin")
    render_template = "poll/plugin/poll_plugin.html"

    def render(self, context, instance, placeholder):
        already_voted = False
        items = None

        poll_id = instance.poll.pk if instance.poll else None
        if poll_id:
            if instance.poll.get_cookie_name() in context['request'].COOKIES:
                already_voted = True
            items = instance.poll.items.all()

        context.update({
            'instance': instance,
            'pollid': poll_id,
            'poll': instance.poll,
            'already_voted': already_voted,
            'items': items
        })
        return context

plugin_pool.register_plugin(PollPluginPublisher)  # register the plugin
