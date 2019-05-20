from django import forms


DISTRICT_CHOICES = (('', '不限'), ('haidian', '海淀'), ('chaoyang', '朝阳'), ('changping', '昌平'),
                    ('miyun', '密云'), ('yanqing', '延庆'), ('fengtai', '丰台'), ('shijingshan', '石景山'),
                    ('mentougou', '门头沟'), ('fangshan', '房山'), ('tongzhou', '通州'), ('shunyi', '顺义'),
                    ('daxing', '大兴'), ('huairou', '怀柔'), ('pinggu', '平谷'), ('dongcheng', '东城'),
                    ('xicheng', '西城'))
PRICE_CHOICES = (('', '不限'), ('rp1', '≤1500元'), ('rp2', '1500-2000元'), ('rp3', '2000-3000元'), ('rp4', '3000-5000元'),
                 ('rp5', '5000-8000元'), ('rp6', '≥8000元'))
BEDROOM_CHOICES = (('', '不限'), ('l0', '一居'), ('l1', '两居'), ('l2', '三居'), ('l3', '四居'))


class HouseChoiceForm(forms.Form):
    district = forms.CharField(label="区域", widget=forms.RadioSelect(choices=DISTRICT_CHOICES))
    price = forms.CharField(label="价格", widget=forms.RadioSelect(choices=PRICE_CHOICES))
    bedroom = forms.CharField(label="庭室", widget=forms.RadioSelect(choices=BEDROOM_CHOICES))

