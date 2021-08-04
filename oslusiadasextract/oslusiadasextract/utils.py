class Utils:
    chants_stanzas = {
        'i': 106,
        'ii': 113,
        'iii': 143,
        'iv': 104,
        'v': 100,
        'vi': 99,
        'vii': 87,
        'viii': 99,
        'ix': 95,
        'x': 156
    }

    base_url = 'https://oslusiadas.org/'

    def parse_scrapy_response(self, response_array):
        response_array[0] = ''
        response_array[1] = ''
        array_with_text = list(filter(lambda x: x != "\n", response_array))
        return array_with_text

    def generate_chants_links(self):
        urls = []
        for chant, number_of_chants in self.chants_stanzas.items():
            url_chant = self.base_url + chant + '/'
            urls.append(url_chant)
            for chant_stanza in range(number_of_chants - 1):
                urls.append(url_chant + str(chant_stanza + 2) + '/')

        return urls

