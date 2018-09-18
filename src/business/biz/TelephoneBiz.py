from ...models.models import Telephone


class TelephoneBiz:

    @staticmethod
    def get_or_none(number):
        return Telephone.get_or_none(number=number)

    @staticmethod
    def save_and_get(number):
        exists = TelephoneBiz.get_or_none(number)
        if not exists:
            model = Telephone(number=number, name='XXXXXXXXXXXX')
            mod = model.save(force_insert=True)
            if mod > 0:
                return TelephoneBiz.get_or_none(number)
        return exists
