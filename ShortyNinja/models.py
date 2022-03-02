def shorten_model(new_url, old_url, date_created):
    sh_model = {
        'new_url': new_url,
        'old_url': old_url,
        'date_created': date_created
    }

    return sh_model


def stats_model(url, clicks, date, old_url, clicks_data):
    st_model = {
        'url_stats': {
            'url': url,
            'clicks': clicks,
            'date_created': date,
            'old_url': old_url
        },

        'clicks_stats': {}

    }

    count = 1

    for row in clicks_data:
        st_model['clicks_stats'][str(count)] = {'ip': row[1], 'date': row[0]}

        count += 1

    return st_model
