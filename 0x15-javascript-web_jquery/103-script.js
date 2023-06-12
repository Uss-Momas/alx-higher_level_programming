window.onload = function () {
  $('INPUT#btn_translate').on('click', function () {
    const $lang = $('INPUT#language_code').val();

    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${$lang}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });

  $('INPUT#language_code').keypress(function (e) {
    const $key = e.which;
    if ($key === 13) {
      const $lang = $('INPUT#language_code').val();
      $.ajax({
        type: 'GET',
        url: `https://hellosalut.stefanbohacek.dev/?lang=${$lang}`,
        success: function (data) {
          $('DIV#hello').text(data.hello);
        }
      });
    }
  });
};
