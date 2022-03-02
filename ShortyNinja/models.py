def shorten_model(new_url, old_url, date_created):
    sh_model = {
        'new_url': new_url,
        'old_url': old_url,
        'date_created': date_created
    }

    return sh_model


def stats_model(url, clicks, date, old_url):
    st_model = {
        'url': url,
        'clicks': clicks,
        'date_created': date,
        'old_url': old_url
    }

    return st_model
