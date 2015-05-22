from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import (
    Button, Quote,
    Gallery, GalleryImage,
    FaqTopic, Faq
)


class ButtonPlugin(CMSPluginBase):
    model = Button
    module = "Widget Box"
    name = "Button"
    render_template = "widgetbox/button.html"


class QuotePlugin(CMSPluginBase):
    model = Quote
    module = "Widget Box"
    name = "Quote"
    render_template = "widgetbox/quote.html"


class GalleryPlugin(CMSPluginBase):
    model = Gallery
    module = "Widget Box"
    name = "Gallery"
    allow_children = True
    child_classes = ["GalleryImagePlugin"]
    render_template = "widgetbox/gallery.html"


class GalleryImagePlugin(CMSPluginBase):
    model = GalleryImage
    module = "Widget Box"
    name = "Gallery Image"
    parent_classes = ["GalleryPlugin"]
    render_template = "widgetbox/gallery-image.html"


class FaqTopicPlugin(CMSPluginBase):
    model = FaqTopic
    module = "Widget Box"
    name = "FAQ Topic"
    allow_children = True
    child_classes = ["FaqPlugin"]

    def get_render_template(self, context, instance, placeholder):
        return instance.style


class FaqPlugin(CMSPluginBase):
    model = Faq
    module = "Widget Box"
    name = "FAQ"
    parent_classes = ["FaqTopicPlugin"]

    def get_render_template(self, context, instance, placeholder):
        return "widgetbox/faq.html"
        # a = dir(instance)
        # b = dir(context)
        c = dir(placeholder)
        parent = dir(instance.get_parent())
        assert False
        return instance.style


plugin_pool.register_plugin(ButtonPlugin)
plugin_pool.register_plugin(QuotePlugin)
plugin_pool.register_plugin(GalleryPlugin)
plugin_pool.register_plugin(GalleryImagePlugin)
plugin_pool.register_plugin(FaqTopicPlugin)
plugin_pool.register_plugin(FaqPlugin)