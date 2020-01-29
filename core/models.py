# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(
		max_length = 50,
		unique = True,
		blank = False,
		null = False
	)
	start = models.DateTimeField(
		blank = False,
		null = False
	)
	end = models.DateTimeField(
		blank = True,
		null = True
	)
class WorkItem(models.Model):
	project = models.ForeignKey(
		Project,
		on_delete=models.PROTECT,
		blank = False,
		null = False
	)
	name = models.CharField(
		max_length = 50,
		unique = True,
		blank = False,
		null = False
	)
	description = models.TextField(
		blank = True,
		null = True
	)
	progress = models.PositiveSmallIntegerField(
		models.MaxValueValidator(100),
		default = 0,
	)
	start = models.DateTimeField(
		blank = False,
		null = False
	)
	# Hours
	time = models.PositiveIntegerField(
		default = 1,
	)
	children = models.ManyToManyField(
		WorkItem,
		on_delete=models.PROTECT
	)
	parents = models.ManyToManyField(
		WorkItem,
		on_delete=models.PROTECT
	)
	def getAllParents(self):
		if self.parents.count() > 0:
			parents = self.parents.all()
			result = parents
			for parent in parents:
				result |= parent.getAllParents()
			return result.distinct()
		return self.parents.none()
	def getAllChildren(self):
		if self.children.count() > 0:
			children = self.children.all()
			result = children
			for child in children:
				result |= child.getAllChildren()
			return result.distinct()
		return self.children.empty()
