from django.shortcuts import render, redirect
from .models import Dashboard
from django.db.models import Q
import datetime
import json


# Create your views here.
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


def rab_profile_index(request):

    # data = {}
    try:
        if request.session['user'] is not None and request.session['admin'] is True:
            return redirect('http://127.0.0.1:8000/admin-profile/')
        elif request.session['user'] is not None and request.session['admin'] is False:

            dash = Dashboard.objects

            y_price = 0
            ly_price = 0

            today = datetime.date.today()
            today_m = today.month
            today_y = today.year

            m_date = dash.filter(Q(DataTime__year=today_y) & Q(DataTime__month=today_m)).all()

            if (today_m - 1) == 0:
                today_y = today.year - 1

            lm_date = dash.filter(Q(DataTime__year=today_y) & Q(DataTime__month=(today_m - 1))).all()

            y_date = dash.filter(Q(DataTime__year=today.year)).all()

            ly_date = dash.filter(Q(DataTime__year=(today.year - 1))).all()

            num_tm = 0

            for e in m_date:
                num_tm += int(e.SaleRev)


            num_lm = 0

            for e in lm_date:
                num_lm += int(e.SaleRev)

            num_pr = 0

            if (num_tm / num_lm * 100) < 100:
                num_pr = '-' + str(round((num_tm / num_lm * 100), 1))
            else:
                num_pr = str(round((num_tm / num_lm * 100), 1))

            all_sales_tm = 0
            all_sales_lm = 0
            all_sales_pr = 0

            for i in m_date:
                all_sales_tm += int(i.SalePrice)

            for i in lm_date:
                all_sales_lm += int(i.SalePrice)

            if (all_sales_tm / all_sales_lm * 100) < 100:
                all_sales_pr = '-' + str(round(all_sales_tm / all_sales_lm * 100, 1))
            else:
                all_sales_pr = str(round(all_sales_tm / all_sales_lm * 100, 1))

            for el in y_date:
                y_price += int(el.SalePrice)

            for el in ly_date:
                ly_price += int(el.SalePrice)

            wprice = 0
            m_price = 0

            for el in m_date:
                m_price += int(el.SalePrice)

            for el in m_date:
                wprice += int(el.SalePrice)

            wprice /= 4
            avg_price_tm = 0
            avg_price_lm = 0
            if num_tm is not 0:
                avg_price_tm = all_sales_tm / num_tm
            if num_lm is not 0:
                avg_price_lm = all_sales_lm / num_lm
            avg_price_pr = 0

            if (avg_price_tm / avg_price_lm * 100) < 100:
                avg_price_pr = '-' + str(round(avg_price_tm / avg_price_lm * 100, 1))
            else:
                avg_price_pr = str(round(avg_price_tm / avg_price_lm * 100, 1))

            data_ty = []

            for el in y_date:
                data_ty.append(int(el.SaleRev))

            data_ly = []

            for el in ly_date:
                data_ly.append(int(el.SaleRev))

            data = {
                'NumSalesTM': num_tm,
                'AllSalesTM': all_sales_tm,
                'AvgPriceTM': round(avg_price_tm, 2),
                'NumSalesLM': float(num_pr),
                'AllSalesLM': float(all_sales_pr),
                'AvgPriceLM': float(avg_price_pr),
                'TMPrice': m_price,
                'TYPrice': y_price,
                'LYPrice': ly_price,
                'WPrice': round(wprice, 2),
                'context_t': json.dumps([{
                    'data_ty': objt.SaleRev,
                }
                    for objt in y_date
                ]),
                'context_l': json.dumps([{
                    'data_ly': objl.SaleRev,
                }
                    for objl in ly_date
                ])
            }
            return render(request, 'rab/rab_index.html', data)

    except KeyError:
        return redirect('http://127.0.0.1:8000/')


