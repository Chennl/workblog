function flask_moment_render(elem) {
    $(elem).text(eval('moment("' + $(elem).data('timestamp') + '").' + $(elem).data('format') + ';'));
    $(elem).removeClass('flask-moment').show();
}
function flask_moment_render_all() {
    $('.flask-moment').each(function() {
        flask_moment_render(this);
        if ($(this).data('refresh')) {
            (function(elem, interval) { setInterval(function() { flask_moment_render(elem) }, interval); })(this, $(this).data('refresh'));
        }
    })
}


function html_moment_render(elem) {
    console.log($(elem).data('timestamp'))
    console.log($(elem).data('format'))
    var texxt= moment( $(elem).data('timestamp')).format( $(elem).data('format') );
   // console.log(eval('moment("' + $(elem).data('timestamp') + '").' + $(elem).data('format') + ';'));
    $(elem).text(texxt);
    $(elem).removeClass('html-moment').show();
}
function html_moment_render_all() {
    $('.html-moment').each(function() {
        html_moment_render(this);
        if ($(this).data('refresh')) {
            (function(elem, interval) { setInterval(function() { html_moment_render(elem) }, interval); })(this, $(this).data('refresh'));
        }
    })
}