from django.shortcuts import render, redirect
from django.views import View
from django.db import connection
import environ
environ.Env.read_env('psql.env')


class Test(View):


    def get(self, request):
        print(environ.Env()('DB_NAME'))
        print(environ.Env()('DB_USER'))
        print(environ.Env()('DB_PASSWORD'))
        print(environ.Env()('SECRET_KEY'))
        return redirect('/')


class DashboardView(View):

    def get(self, request):
        with connection.cursor() as c:
            user_data = c.execute(
                '''
select DISTINCT au.username as uname, sum(t.price)
from account_user au,
(select sh.user_id as uid, price
from good_good gg
inner join store_history sh
on gg.id == sh.good_id) as t
where au.id == t.uid
GROUP BY uname;
                '''
            ).fetchall()

            store_data = c.execute(
                '''
select DISTINCT full_address as adrs, sum(price) as price, count(user_id) as uid
from good_good gg
inner join
(select *
from store_store ss
inner join store_history sh
on ss.id == sh.store_id) as t
on gg.id == t.good_id
GROUP BY adrs
                '''
            ).fetchall()
            print(store_data)
            return render(request, 'dashboard.html', {
                'discount_table': user_data,
                'store_table': store_data,
            })
