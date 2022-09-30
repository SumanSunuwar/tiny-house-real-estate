import json

from rest_framework.renderers import JSONRenderer


class ProfileJSONRenderer(JSONRenderer):
    """JSON renderer for profile objects"""
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get("errors", None)
        print("printting errors",errors)
        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)

        return json.dumps({"profile": data})