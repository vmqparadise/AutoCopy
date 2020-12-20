class WordToHtmlDotNet:
    waiting_time = 2

    html_cleaner = dict(
        url = 'https://wordtohtml.net/',
        html_txtbox_class_name = 'CodeMirror-scroll',
        word_txtbox_id = 'elm1_ifr',
        clear_button_class_name = 'clearButton',
        edit_id = 'mceu_29-open',
        edit_select_all_id = 'mceu_59',
        edit_copy_id = 'mceu_55',
        )

    html_file = dict(
        name = 'urls.txt'
        )

    tag_to_get = dict(
        tag_name = 'tag_name',
        att_name = 'attribute_name',
        att_value = 'attribute_value'
        )
