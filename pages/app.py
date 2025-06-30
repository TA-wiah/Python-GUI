import pyvisual as pv
from ui.ui import create_ui

# ===================================================
# ================ 1. LOGIC CODE ====================
# ===================================================

# (Your logic code here)

# ===================================================
# ============== 2. EVENT BINDINGS ==================
# ===================================================


def attach_events(ui):
    """
    Bind events to UI components.
    :param ui: Dictionary containing UI components.
    """
    pass

# ===================================================
# ============== 3. MAIN FUNCTION ==================
# ===================================================


def main():
    app = pv.PvApp()
    ui = create_ui()
    attach_events(ui)
    ui["window"].show()
    app.run()


if __name__ == '__main__':
    main()
