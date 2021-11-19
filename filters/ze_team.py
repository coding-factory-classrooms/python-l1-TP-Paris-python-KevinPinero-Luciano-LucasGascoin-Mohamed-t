import cv2
import logger


org = (50, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 1
color = (255, 255, 0)
text = "Lucas | Mohamed | Kevin | Luciano"


def ze_team_filter(image):
    """[function for applying ZeTeam filter to image]

        Args:
            image ([file.jpg or .png or .jpeg]): [image]

        Returns:
            [image]: [filtered image with ZeTeam filter applied]
    """
    img_ze_team = cv2.putText(image, text, org, font, font_scale, color, thickness)
    logger.filter_log("ZeTeam")
    return img_ze_team

