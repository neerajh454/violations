from rest_framework import serializers
from .models import Type, Violation, Action, Comment

class TypeSerializer(serializers.Serializer):
	shortcode = serializers.CharField(required=True, allow_blank=False, max_length=100)
	display = serializers.CharField(required=False, allow_blank=True, max_length=100)
	severity = serializers.CharField(required=False, allow_blank=True, max_length=100)
	group = serializers.CharField(required=False, allow_blank=True, max_length=100)
	configurable_counts = serializers.CharField(required=False, allow_blank=True, max_length=100)

	def validate(self, data):

		if 'shortcode' in data:
			data['shortcode'] = data['shortcode'].lower()

			if 'display' not in data:
				data['display'] = data['shortcode'].replace('_',' ').title()
			
			if 'severity' in data: ## -- Make the text to lower case on save -- ##
				data['severity'] = data['severity'].lower()

			try:
				data['instance'] = Type.objects.get(shortcode=data['shortcode']) ## -- If data exist, then execute Update of it -- ##
				data['id'] = data['instance'].id ## -- Pass  ID if data exist or not -- ##
			except:
				pass
		else:
			raise serializers.ValidationError({
				'status': 417, ## -- Expectation Failed -- ##
				'message': 'Required Params not passed -> shortcode, display'
			})
		return data

	def create(self, validated_data):
		"""
		Create and return a new `Type` instance, given the validated data.
		"""
		return Type.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Type` instance, given the validated data.
		"""
		#instance.shortcode = validated_data.get('shortcode', instance.shortcode)
		instance.display = validated_data.get('display', instance.display)
		if 'severity' in validated_data:
			instance.severity = validated_data.get('severity', instance.severity).lower()
		instance.group = validated_data.get('group', instance.group)
		instance.configurable_counts = validated_data.get('configurable_counts', instance.configurable_counts)
		instance.save()

		return instance

	class Meta:
		model = Type
		fields = ('id', 'shortcode', 'display', 'severity', 'group', 'configurable_counts')


class ViolationSerializer(serializers.Serializer):
	vio_id = serializers.IntegerField(required=False, min_value=1)
	vio_type = serializers.CharField(required=True, allow_blank=False, max_length=100)
	who_id = serializers.IntegerField(min_value=1)
	who_type = serializers.CharField(required=True, allow_blank=False, max_length=100)
	who_meta = serializers.CharField(required=False, allow_blank=False, max_length=5000)#serializers.JSONField(binary=False)
	whom_id = serializers.IntegerField(min_value=1)
	whom_type = serializers.CharField(required=True, allow_blank=False, max_length=100)
	whom_meta = serializers.CharField(required=False, allow_blank=False, max_length=5000)#serializers.JSONField(binary=False)
	cc_list = serializers.ListField(child=serializers.IntegerField(min_value=0))#, min_length=0)
	cc_list_meta = serializers.ListField(child=serializers.CharField(required=False, allow_blank=False, max_length=5000))#, min_length=0)#serializers.ListField(child=serializers.JSONField(binary=False))#, min_length=0)
	bcc_list = serializers.ListField(child=serializers.IntegerField(min_value=0))#, min_length=0)
	bcc_list_meta = serializers.ListField(child=serializers.CharField(required=False, allow_blank=False, max_length=5000))#, min_length=0)#serializers.ListField(child=serializers.JSONField(binary=False))#, min_length=0)
	status = serializers.CharField(required=True, allow_blank=False, max_length=100)
	violation_nature = serializers.CharField(required=False, allow_blank=False, max_length=100)

	def validate(self, data):
		list_param = ['who_id', 'who_type', 'whom_id', 'whom_type', 'status', 'vio_type']

		if not all (k in data for k in list_param):
			raise serializers.ValidationError({
				'status': 417, ## -- Expectation Failed -- ##
				'message': "Respective Params required -> 'who_id', 'who_type', 'whom_id', 'whom_type', 'status', 'vio_type'"
			})
		else:
			try:
				if 'vio_id' in data and data['vio_id']:
					data['instance'] = Violation.objects.get(id=data['vio_id'])
			except:
				pass

		return data

	def create(self, validated_data):
		"""
		Create and return a new `Type` instance, given the validated data.
		"""
		type_data = Type.objects.get(shortcode=validated_data.pop('vio_type')) ## -- Get Type Details using Type ID -- ##
		return Violation.objects.create(vio_type=type_data, **validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Type` instance, given the validated data.
		"""
		#instance.vio_type = validated_data.get('vio_type', instance.vio_type)
		#instance.who_id = validated_data.get('who_id', instance.who_id)
		#instance.who_type = validated_data.get('who_type', instance.who_type)
		instance.who_meta = validated_data.get('who_meta', instance.who_meta)
		#instance.whom_id = validated_data.get('whom_id', instance.whom_id)
		#instance.whom_type = validated_data.get('whom_type', instance.whom_type)
		instance.whom_meta = validated_data.get('whom_meta', instance.whom_meta)
		instance.cc_list = validated_data.get('cc_list', instance.cc_list)
		instance.cc_list_meta = validated_data.get('cc_list_meta', instance.cc_list_meta)
		instance.bcc_list = validated_data.get('bcc_list', instance.bcc_list)
		instance.bcc_list_meta = validated_data.get('bcc_list_meta', instance.bcc_list_meta)
		instance.status = validated_data.get('status', instance.status)
		instance.violation_nature = validated_data.get('violation_nature', instance.violation_nature)
		instance.save()

		return instance

	class Meta:
		model = Violation
		fields = ('id', 'who_id', 'who_type', 'who_meta', 'whom_id', 'whom_type', 'whom_meta', 'cc_list', 'cc_list_meta', 'bcc_list', 'bcc_list_meta', 'status', 'violation_nature')


class CommentSerializer(serializers.Serializer):
	violation_id = serializers.IntegerField(min_value=1)
	who_id = serializers.IntegerField(min_value=1)
	who_meta = serializers.CharField(required=False, allow_blank=False, max_length=5000)#serializers.JSONField(binary=False)
	comment = serializers.CharField(required=True, allow_blank=True, max_length=100)

	def validate(self, data):
		list_param = ['violation_id', 'who_id', 'comment']

		if not all (k in data for k in list_param):
			raise serializers.ValidationError({
				'status': 417, ## -- Expectation Failed -- ##
				'message': "'violation_id', 'who_id' and 'comment' parameters are required"
			})
		return data

	def create(self, validated_data):
		"""
		Create and return a new `Comment` instance, given the validated data.
		"""
		
		violation_data = Violation.objects.get(id=validated_data.pop('violation_id')) ## -- Get Violation Details using Vioaltion ID -- ##
		return Comment.objects.create(violation=violation_data, **validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Comment` instance, given the validated data.
		"""
		#instance.violation_id = validated_data.get('violation_id', instance.violation_id)
		instance.who_id = validated_data.get('who_id', instance.who_id)
		instance.who_meta = validated_data.get('who_meta', instance.who_meta)
		instance.comment = validated_data.get('comment', instance.comment)
		instance.save()

		return instance

	class Meta:
		model = Comment
		fields = ('id', 'violation_id', 'who_id', 'who_meta', 'comment', 'timestamp')


class ActionSerializer(serializers.Serializer):
	vio_id = serializers.IntegerField(min_value=1)
	who_id = serializers.IntegerField(required=True, min_value=1)
	who_meta = serializers.CharField(required=False, allow_blank=False, max_length=5000)#serializers.JSONField(binary=False)
	what = serializers.CharField(required=True, allow_blank=False, max_length=100)
	what_meta = serializers.CharField(required=False, allow_blank=False, max_length=5000)#serializers.JSONField(binary=False)

	def validate(self, data):
		list_param = ['vio_id', 'who_id', 'what', 'what_meta']

		if not all (k in data for k in list_param):
			raise serializers.ValidationError({
				'status': 417, ## -- Expectation Failed -- ##
				'message': "'vio_id', 'who_id', 'what' and 'what_meta' parameters are required"
			})
		else:
			data_obj = Action.objects.filter(violation__id=data['vio_id'], who_id=data['who_id'], what=data['what'])
			
			if data_obj.exists():
				raise serializers.ValidationError({
					'status': 409, ## -- Conflict -- ##
					'message': 'This user already taken an action on this violation'
				})
		return data

	def create(self, validated_data):
		"""
		Create and return a new `Action` instance, given the validated data.
		"""
		violation_data = Violation.objects.get(id=validated_data.pop('vio_id')) ## -- Get Violation Details using Vioaltion ID -- ##
		return Action.objects.create(violation=violation_data, **validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Action` instance, given the validated data.
		"""
		#instance.vio_id = validated_data.get('vio_id', instance.vio_id)
		#instance.who_id = validated_data.get('who_id', instance.who_id)
		instance.who_meta = validated_data.get('who_meta', instance.who_meta)
		instance.what = validated_data.get('what', instance.what)
		instance.what_meta = validated_data.get('what_meta', instance.what_meta)
		instance.save()

		return instance

	class Meta:
		model = Action
		fields = ('id', 'violation', 'who_id', 'who_meta', 'what', 'what_meta', 'timestamp')