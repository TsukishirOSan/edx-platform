"""Edx footer API

"""
from django.http import HttpResponse
import logging
from util.json_request import JsonResponse
from django.conf import settings
from django.utils.translation import ugettext as _
from microsite_configuration import microsite

log = logging.getLogger("edx.footer")


def get_footer():

    site_name = microsite.get_value('SITE_NAME', settings.SITE_NAME)
    context = dict()

    context["logo_img"] = "{site_name}/sites/all/themes/atedx/images/edx-logo-footer.png".format(site_name=site_name)
    context["social_links"] = social_links()
    context["about_links"] = about_edx_link(site_name)

    return JsonResponse({"footer": context}, 200)


def social_links():

    return [
        {
            "provider": "facebook",
            "title": _("Facebook"),
            "url": "http://www.facebook.com/EdxOnline"
        },
        {
            "provider": "twitter",
            "title": _("Twitter"),
            "url": "https://twitter.com/edXOnline"
        },
        {
            "provider": "linkedin",
            "title": _("LinkedIn"),
            "url": "http://www.linkedin.com/company/edx"
        },
        {
            "provider": "google",
            "title": _("Google+"),
            "url": "https://plus.google.com/+edXOnline"
        },
        {
            "provider": "tumblr",
            "title": _("Tumblr"),
            "url": "http://edxstories.tumblr.com/"
        },
        {
            "provider": "meetup",
            "title": _("Meetup"),
            "url": "http://www.meetup.com/edX-Global-Community"
        },
        {
            "provider": "reddit",
            "title": _("Reddit"),
            "url": "http://www.reddit.com/r/edx"
        },
        {
            "provider": "youtube",
            "title": _("Youtube"),
            "url": "https://www.youtube.com/user/edxonline?sub_confirmation=1"
        },
    ]


def about_edx_link(site_name):

    return [
        {
            "title": _("About"),
            "url": "{}/about-us".format(site_name)
        },
        {
            "title": _("News & Announcements"),
            "url": "{}/news-announcements".format(site_name)
        },
        {
            "title": _("Contact"),
            "url": "{}/contact-us".format(site_name)
        },
        {
            "title": _("FAQs"),
            "url": "{}/about/student-faq".format(site_name)
        },
        {
            "title": _("edX Blog"),
            "url": "{}/edx-blog".format(site_name)
        },
        {
            "title": _("Donate to edX"),
            "url": "{}/donate".format(site_name)
        },
        {
            "title": _("Jobs at edX"),
            "url": "{}/jobs".format(site_name)
        },
        {
            "title": _("Site Map"),
            "url": "{}/sitemap".format(site_name)
        },
    ]


def footer_heading():
    return ""