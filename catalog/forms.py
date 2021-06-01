from django.forms import ModelForm, TextInput, FileInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _
from .models import Catalog


class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ['ProductName', 'ProductMaker', 'ProductBrand', 'ProductPrice', 'ProductCategory', 'ProductFeatures',
                  'ProductDescription', 'ProductImage', 'ProductMetaTittle',
                  'ProductMetaKeywords', 'ProductMetaDescription']

        widgets = {
            "ProductName": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Название товара"
            }),
            "ProductMaker": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Производитель"
            }),
            "ProductBrand": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Бренд"
            }),
            "ProductPrice": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Цена"
            }),
            "ProductCategory": Select(attrs={'class': 'form-control select2'}),
            "ProductFeatures": Select(attrs={'class': 'form-control select2'}),
            "ProductImage": FileInput(attrs={'class': 'dropzone', 'multiple': True, 'enctype': 'multipart/form-data'}),
            "ProductDescription": Textarea(attrs={

                "class": "form-control",
                "id": "productdesc",
                "rows": 5,
                "placeholder": "Описание товара"
            }),
            "ProductMetaTittle": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Мета заголовок",
                "id": "metatitle"
            }),
            "ProductMetaKeywords": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Мета ключевые слова",
                "id": "metakeywords"
            }),
            "ProductMetaDescription": Textarea(attrs={

                "class": "form-control",
                "placeholder": "Мета описание",
                "id": "metadescription",
                "rows": 5
            }),

        }

        labels = {
            "ProductName": _("Название товара"),
            "ProductMaker": _("Производитель"),
            "ProductBrand": _("Бренд"),
            "ProductPrice": _("Цена"),
            "ProductCategory": _("Категория"),
            "ProductFeatures": _("Под-категория"),
            "ProductDescription": _("Описание товара"),
            "ProductMetaTittle": _("Мета заголовок"),
            "ProductMetaKeywords": _("Мета ключевые слова"),
            "ProductMetaDescription": _("Мета описание"),
        }

    class Media:
        js = ('js/dropzone.min.js',)