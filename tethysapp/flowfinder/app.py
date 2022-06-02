from tethys_sdk.base import TethysAppBase, url_map_maker


class Flowfinder(TethysAppBase):
    """
    Tethys app class for Flow Finder.
    """

    name = 'Flow Finder'
    index = 'flowfinder:home'
    icon = 'flowfinder/images/icon.gif'
    package = 'flowfinder'
    root_url = 'flowfinder'
    color = '#2c3e50'
    description = 'Find the daily discharge for any watershed in the world.'
    tags = '"Hydrology", "Discharge", Stream flow"'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='flowfinder',
                controller='flowfinder.controllers.home'
            ),
            UrlMap(
                name='downloadElevation',
                url='downloadElevation/',
                controller='flowfinder.delineateWatershed.download_ee_elevation'
            ),
            UrlMap(
                name='delineateWatershed',
                url='delineateWatershed/',
                controller='flowfinder.delineateWatershed.delineate_watershed'
            ),
            UrlMap(
                name='getDataImage',
                url='getDataImage/',
                controller='flowfinder.earthEngine.get_data_tiles'
            ),
            UrlMap(
                name='getTimeSeries',
                url='getTimeSeries/',
                controller='flowfinder.earthEngine.plot_time_series'
            ),
            UrlMap(
                name='getElevationImage',
                url='getElevationImage/',
                controller='flowfinder.earthEngine.get_elevation_tiles'
            )
        )

        return url_maps
