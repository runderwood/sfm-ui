from django_filters import FilterSet, CharFilter
from ui.models import Warc


class WarcFilter(FilterSet):
    # Allows queries like /api/v1/warcs/?seedset=39c00280274a4db0b1cb5bfa4d527a1e
    seedset = CharFilter(name="harvest__seed_set__seedset_id")

    class Meta:
        model = Warc
        fields = ['seedset']