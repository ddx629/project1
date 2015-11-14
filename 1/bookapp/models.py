# -*- coding: utf-8 -*-
from django.db import models

class Author(models.Model):
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        
    AuthorID = models.CharField('作者ID',max_length=20,primary_key=True)
    Name = models.CharField('姓名',max_length=20)
    Age = models.IntegerField('年龄',max_length=3,blank=True)
    Country = models.CharField('国家',max_length=20,blank=True)
    
    def __unicode__(self):
        return str(self.Name)

class Book(models.Model):
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name
        
    ISBN = models.CharField('ISBN',max_length=13,primary_key=True)
    Title = models.CharField('书名',max_length=50)
    AuthorID = models.ForeignKey(Author, related_name='author_book')
    Publisher = models.CharField('出版社',max_length=30,blank=True)
    PublishDate = models.CharField('出版日期',max_length=20,blank=True)
    Price = models.CharField('定价',max_length=20,blank=True)
    
    def __unicode__(self):
        return str(self.Title)
    
