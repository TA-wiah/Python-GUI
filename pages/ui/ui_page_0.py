import pyvisual as pv


def create_page_0_ui(window,ui):
    """
    Create and return UI elements for Page 0.
    :param container: The page widget for Page 0.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["TextInput_0"] = pv.PvTextInput(container=window, x=417, y=146, width=127,
        height=40, background_color=(255, 255, 255, 1), is_visible=True, placeholder='First Name',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/BaiJamjuree/BaiJamjuree.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='Text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["TextInput_1"] = pv.PvTextInput(container=window, x=564, y=146, width=116,
        height=40, background_color=(255, 255, 255, 1), is_visible=True, placeholder='Last Name',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/BaiJamjuree/BaiJamjuree.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='Text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["Button_2"] = pv.PvButton(container=window, x=456, y=282, width=200,
        height=50, text='Submit', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(56, 136, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=25, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["TextInput_3"] = pv.PvTextInput(container=window, x=417, y=201, width=264,
        height=40, background_color=(255, 255, 255, 1), is_visible=True, placeholder='Password',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["Checkbox_4"] = pv.PvCheckbox(container=window, x=550, y=241, width=135,
        height=28, text='Accept our Terms', is_checked=True, checked_color=(3, 162, 30, 1),
        unchecked_color=(214, 214, 214, 1), checkmark_color=(255, 255, 255, 1), checkmark_size=10, checkbox_size=12,
        corner_radius=10, checkmark_type='✓', border_color=(0, 0, 0, 1), border_thickness=0,
        spacing=10, font='assets/fonts/Poppins/Poppins.ttf', font_size=11, font_color=(0, 0, 0, 1),
        bold=False, italic=False, underline=False, strikeout=False,
        paddings=(5, 0, 0, 0), is_visible=True, opacity=1, tag=None,
        on_change=None)

    ui_page["Checkbox_5"] = pv.PvCheckbox(container=window, x=417, y=241, width=131,
        height=27, text='Stay logged in', is_checked=False, checked_color=(31, 31, 31, 1),
        unchecked_color=(214, 214, 214, 1), checkmark_color=(0, 0, 0, 1), checkmark_size=10, checkbox_size=13,
        corner_radius=10, checkmark_type='✓', border_color=(0, 0, 0, 1), border_thickness=0,
        spacing=10, font='assets/fonts/Poppins/Poppins.ttf', font_size=12, font_color=(0, 0, 0, 1),
        bold=True, italic=False, underline=False, strikeout=False,
        paddings=(5, 0, 0, 0), is_visible=True, opacity=1, tag=None,
        on_change=None)

    ui_page["Text_6"] = pv.PvText(container=window, x=420, y=16, width=127,
        height=56, idle_color=(171, 84, 220, 0), text='SIGN UP', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Montserrat/Montserrat.ttf', font_size=25,
        font_color=(255, 255, 255, 1), bold=True, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_7"] = pv.PvText(container=window, x=585, y=357, width=90,
        height=14, idle_color=(166, 158, 158, 0), text='Click Here', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/ZillaSlab/ZillaSlab.ttf', font_size=16,
        font_color=(1, 103, 255, 1), bold=True, italic=False, underline=True,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_8"] = pv.PvText(container=window, x=417, y=357, width=168,
        height=14, idle_color=(238, 225, 255, 0), text='Already have an account', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Rubik/Rubik.ttf', font_size=13,
        font_color=(255, 255, 255, 1), bold=True, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Icon_9"] = pv.PvIcon(container=window, x=2, y=1, width=30,
        height=30, idle_color=(75, 75, 75, 1), preserve_original_colors=False, icon_path='assets/icons/333e6fa6e1.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["Icon_10"] = pv.PvIcon(container=window, x=2, y=44, width=480,
        height=356, idle_color=(12, 111, 123, 1), preserve_original_colors=True, icon_path='assets/icons/280d0a3e23.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["TextInput_11"] = pv.PvTextInput(container=window, x=417, y=78, width=260,
        height=40, background_color=(255, 255, 255, 1), is_visible=True, placeholder='Username',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/BaiJamjuree/BaiJamjuree.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='Text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["Rectangle_12"] = pv.PvRectangle(container=window, x=409, y=19, width=290,
        height=366, idle_color=None, border_color=(0, 0, 0, 1), border_thickness=2,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    return ui_page
