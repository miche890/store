from marketing.models import Banners, PromotionalVideo


def marketing_context(request):
    banners = Banners.objects.all()
    promotional_videos = PromotionalVideo.objects.filter(active=True)
    banners_highlight = Banners.objects.filter(highlight=True)
    return {
        'banners': banners,
        'videos': promotional_videos,
        'banners_highlight': banners_highlight
    }
