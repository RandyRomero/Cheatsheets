### Serializer with one more field

For example I have a model serializer where I established fields via meta calss.
And I want to make another one, almost the same serilizer, but with one extra field.
How whould I do it?

For example I have this serializer:
```python
class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Whatever
        fields = ('created','modified','client_time','user',)
```

and I want another one, say, ChildSerializer, with one additional field: id

answer

That's how it's done:
```python
class ChildSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta): 
        fields = BaseSerializer.Meta.fields + ('id',)
```

question id: 0069004b-bbbd-4465-a835-36adfda80cea