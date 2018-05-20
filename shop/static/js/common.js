$(function() {

    $('[data-action-to-cart]').click(function(e) {
        const el = e.target;
        const data = el.dataset;

        $.get(data.actionToCart)
            .then(function(res) {
                if (res.count) updateCartCount(res.count);
                showAlert('Товар успешно добавлен в корзину', 'success');
            })
            .catch(function(err) {
                showAlert('Не удалось добавить товар в корзину', 'danger');
            });
    });

    $('[data-action-remove-from-cart]').click(function(e) {
        const el = e.target;
        const data = el.dataset;

        $.get(data.actionRemoveFromCart)
            .then(function(res) {
                if (res.count) updateCartCount(res.count);
                if (res.total) updateCartTotal(res.total);

                const row = el.closest('.product_row');
                row && row.fadeOut(function() {
                        row.remove();
                    });
            })
            .catch(function(err) {
                showAlert('Ошибка сервера', 'danger');
            });

        e.preventDefault();
    });

    function showAlert(msg, type) {
        type = type || 'success';

        const el = $('<div></div>', {
            'class': 'd-inline-block shadow alert alert-' + type,
            text: msg
        });

        const wrapper = $('<div></div>', {
            'class': 'text-center',
            style: 'pointer-events:none'
        });

        wrapper.append(el);
        $('#notify_container').append(wrapper);

        el.hide();
        el.fadeIn();

        setTimeout(function (el) {
            el.fadeOut(function() {
                el.remove();
                wrapper.remove();
            });
        }.bind(null, el), 3000);
    }

    function updateCartCount(count) {
        $('[data-cart-count]').text(count);
    }

    function updateCartTotal(price) {
        $('[data-cart-total-price]').text(price);
    }

});