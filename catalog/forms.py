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
                "placeholder": "Product Name"
            }),
            "ProductMaker": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Manufacturer Name"
            }),
            "ProductBrand": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Manufacturer Brand"
            }),
            "ProductPrice": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Price"
            }),
            "ProductCategory": Select(attrs={'class': 'form-control select2'}),
            "ProductFeatures": Select(attrs={'class': 'form-control select2'}),
            "ProductDescription": Textarea(attrs={

                "class": "form-control",
                "id": "productdesc",
                "rows": 5,
                "placeholder": "Product Description"
            }),
            "ProductImage": FileInput(attrs={'method': "post", 'multiple': 'True'}),
            "ProductMetaTittle": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Meta title",
                "id": "metatitle"
            }),
            "ProductMetaKeywords": TextInput(attrs={

                "class": "form-control",
                "placeholder": "Meta Keywords",
                "id": "metakeywords"
            }),
            "ProductMetaDescription": Textarea(attrs={

                "class": "form-control",
                "placeholder": "Meta Description",
                "id": "metadescription",
                "rows": 5
            })
        }

        labels = {
            "ProductName": _("Product Name"),
            "ProductMaker": _("Manufacturer Name"),
            "ProductBrand": _("Manufacturer Brand"),
            "ProductPrice": _("Price"),
            "ProductCategory": _("Product Category"),
            "ProductFeatures": _("Subcategories"),
            "ProductDescription": _("Product Description"),
            "ProductImage": _("Product Image"),
            "ProductMetaTittle": _("Meta title"),
            "ProductMetaKeywords": _("Meta Keywords"),
            "ProductMetaDescription": _("Meta Description"),
        }