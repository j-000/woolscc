from server import ma
from .URL import URL

class URLSerializer(ma.SQLAlchemySchema):
    class Meta:
        model = URL
        fields = ['id', 'timestamp', 'original_url', 'follow_url', 'active', 'identifier']