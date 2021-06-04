function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    // Получаем данные из формы
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.getElementById('filters');
    div.innerHTML = output;
}

let html = '\
{{#filtered}}\
    <div class="col-xl-4 col-sm-6">\
        <a href="/catalog/{{ ProductId }}" class="text-dark">\
            <div class="product-box">\
                <div class="product-img">\
                    <img src="media/{{ ProductImage }}" alt=""\
                         class="mx-auto d-block" width="195" height="195">\
                </div>\
                <div class="text-center">\
                    <p class="font-size-12 mb-1">{{ get_ProductFeatures_display }}</p>\
                    <h5 class="font-size-15">{{ ProductName }}</h5>\
                    <h5 class="mt-3 mb-0">₽ {{ ProductPrice }}</h5>\
                </div>\
            </div>\
        </a>\
    </div>\
{{/filtered}}'