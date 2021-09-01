from rest_framework import serializers
from rodin.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'news_title',
                  'news_description',
                  'is_published')
