### You have a viewset. How to dispatch something right before or right after creation of the resource? 

For example, if you want to send an event.

In your class, based on some ViewSet class, you need override this method:

```python
from rest_framework.viewsets import ModelViewSet

class YourViewSet(ModelViewSet):

    def perform_create(self, serializer):
        # do whatever you want beforehand
        super().perform_create(serializer)
        # do whatever you want afterwards
```

question id: e9395b1d-fd66-4cd6-a565-80b4aa8fa101


### You have a viewset. How to dispatch something right before or right after updating of the resource?

For example, if you want to send an event.

In your class, based on some ViewSet class, you need override this method:

```python
from rest_framework.viewsets import ModelViewSet

class YourViewSet(ModelViewSet):

    def perform_update(self, serializer):
        # do whatever you want beforehand
        super().perform_update(serializer)
        # do whatever you want afterwards
```

question id: 9ec0338b-8164-4f3e-9415-0dfb6272f0a2

### You have a viewset. How to dispatch something right before or right after deleting of the resource?

For example, if you want to send an event.

In your class, based on some ViewSet class, you need override this method:


```python
from rest_framework.viewsets import ModelViewSet

class YourViewSet(ModelViewSet):

    def perform_destroy(self, instance):
        # do whatever you want beforehand
        super().perform_destroy(instance)
        # do whatever you want afterwards
```

question id: 086e8034-33fb-41ea-bf52-6ed41f52b3ba

### In a ViewSet in perform_create(self, serializer) or perform_update(self, serializer) - how to get path or the request?

For example `/api/v1/users/2/skills/3/`

```python
from rest_framework.viewsets import ModelViewSet

class YourViewSet(ModelViewSet):

    def perform_update(self, serializer):
        path = serializer.request.path  # contains the path
        super().perform_update(serializer)
```

question id: 453a2a9b-a6bf-4a51-8077-d82ce5b804dd


### In a ViewSet in perform_create(self, serializer) or perform_update(self, serializer) - how to get payload of the request?


```python
from rest_framework.viewsets import ModelViewSet

class YourViewSet(ModelViewSet):

    def perform_update(self, serializer):
        data = serializer.request.data  # contains the data as a dict
        super().perform_update(serializer)
```

question id: 69c6ec04-0e34-479e-8f96-25b2b2d71909

### In a ViewSet in perform_create(self, serializer) or perform_update(self, serializer) - how to get user of the request?


```python
from rest_framework.viewsets import ModelViewSet

class YourViewSet(ModelViewSet):

    def perform_update(self, serializer):
        user = serializer.request.user  
        super().perform_update(serializer)
```

question id: ee17802d-4d67-4b4a-b907-69f3b1ea5a82


### How to validate whether some parent table field equals to something when patching child table?

For example your have user and user_profiles tables via one-to-one. You are patching some field in user_profiles, 
but for that you want to make sure that a specific field in user table in a valid state. How would you do that?

```python
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class PforileSerializer(serializers.Serializer):
    ...
    
    def validate_field_that_your_are_patching(self, value):
        if not self.instance.user.some_field == 'something':
            raise ValidationError
```

question id: 

### In user_profile serializer on validation check that user have specific skill

You have users and user profiles tables connected via one-to-one relationship. 
Also you have m2m table which connects users and skills. So user has attribute skills which has attribute name.
In user_profiles table you have field `position`.
You need to check when somebody wants to set this position of a user to specific_position, whether this user has specific
skill `skill_name`. How to do that?

answer

You have to add to ProfileSerializer method validate_position and there check the skills of user:

Hint: in your serializer class you have self.instance attribute, in your case it is Profile(). Through this 
self.instance you can get user of this instance, and from user you can get user skill which is the manager that
allows you to filter through skill of this user


```python
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class PforileSerializer(serializers.Serializer):
    ...
    
    def validate_position(self, value):
        if value != 'specific_position':
            if not self.instance.user.skills.filter(name='specific_skill').exists():
                raise ValidationError
```


### How to get instance of your object in serializer?

In short: through self.instance attribute of the serializer

Verbose:

Serializer has special attribute - self.instance. Through it you can get access to other attributes of your objects
or to attributes of related objects. There is an example:

```python
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class PforileSerializer(serializers.Serializer):
    ...
    
    def validate_position(self, value):
        if not self.instance.user.skills.filter(name='specific_skill').exists():
            raise ValidationError
```

question id: 15b71fbe-4e86-40b4-b10b-81e6dc72e13f


### What is DRF and what does it bring to Django?

answer
DRF is a powerful and flexible toolkit for building Web APIs.
It adds to Django such things as: 
- serializers 
- class-based views and viewsets (that allow you to encanpsulate REST API methods like GET, POST and the rest in one 
  View)
- some other useful things

question id: 08db85c5-f7a7-4bce-9140-92d58fd5b933


### How to set checks like allow_blank=True on a field in ModelSerializer?

```python
class SomeModelSerializer(serializers.ModelSerializer):
    """Some model serializer."""

    supplier_id = serializers.IntegerField(source="order.supplier_id")
    
    class Meta:
        model = SomeModel
        fields = (
            "id",
            "guid",
            "name",
            "supplier_id",
            "deleted_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "deleted_at", "created_at", "updated_at")
```

For example, you want to allow 'supplier_id' or 'name' to be null, how would you do that?  

answer
If the field has already been explicitly declared on the serializer class, you set
this check where you have declared this field like 

```python
supplier_id = serializers.IntegerField(source="order.supplier_id", allow_null=True)
```

Otherwise, you declare extra_kwargs attribute in class Meta and use it like this:
```python
class SomeModelSerializer(serializers.ModelSerializer):
    """Some model serializer."""

    supplier_id = serializers.IntegerField(source="order.supplier_id")
    
    class Meta:
        model = SomeModel
        fields = (
            "id",
            "guid",
            "name",
            "supplier_id",
            "deleted_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "deleted_at", "created_at", "updated_at")
        extra_kwargs = {
            "name": {"allow_null": True},
            "guid": {"required": False, "default": None},
        }
```

https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments

question id: 52c8cd91-f351-4611-8c2b-1d858c76feb5


### What are default value for a drf serializer for arguments 'required', 'allow_null', 'allow_blank', 'read_only'?

answer

- required=None (required = True if required is None and default is empty else False)
- allow_null=False
- allow_blank=False
- read-only=False

question id: 257fe0ff-982d-4c17-9c5c-95c9b6594199


### Pass exception from Model to DRF Serializer 

For example, you have your model Blog and withing save() method you validate something.
In case validation failed, how would you return via API to the requester status code 400 with sensible 
error message?

answer

You just have to raise rest_framework.serializers.ValidationError.
If you raise some other error, you will get a 500 as a server response.
However, if you raise (ValidationError("That what's wrong with your request")) from rest_framework.serializers,
drf serializer will catch it and return 400 with your message. 

```python
from rest_framework.serializers import ValidationError

def save(self, **kwargs):
    try:
        super().save(**kwargs)
    except ModelError as e:
        raise serializers.ValidationError(e)
```

https://stackoverflow.com/questions/54061030/django-return-serializer-validationerror-in-model-save-method

question id: 27f602a4-94ea-489e-9fd7-6d6fdc8b1ddd