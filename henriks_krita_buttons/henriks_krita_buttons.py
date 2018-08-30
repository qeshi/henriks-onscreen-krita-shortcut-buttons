#BBD's Krita Script Starter Feb 2018
from krita import DockWidget, DockWidgetFactory, DockWidgetFactoryBase
from PyQt5.QtWidgets import *
import sys


DOCKER_NAME = 'Henriks buttons'
DOCKER_ID = 'henriks_buttons'

class HenriksOnscreenKritaShortcutButtons(DockWidget):


    def undo(self):
        Krita.instance().action('edit_undo').trigger()

    def previous_brush(self):
        Krita.instance().action('previous_preset').trigger()

    def redo(self):
        Krita.instance().action('edit_redo').trigger()

    def reset_zoom(self):
        Krita.instance().action('zoom_to_100pct').trigger()

    def rotate_left(self):
        Krita.instance().action('rotate_canvas_left').trigger()

    def rotate_right(self):
        Krita.instance().action('rotate_canvas_right').trigger()

    def mirror_canvas(self):
        Krita.instance().action('mirror_canvas').trigger()

    def only_canvas(self):
        Krita.instance().action('view_show_canvas_only').trigger()

    def reset_canvas_rotation(self):
        Krita.instance().action('reset_canvas_rotation').trigger()

    def create_button(self, text, parentWidget, action):
        button = QPushButton(text, parentWidget)
        button.clicked.connect(action)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return button

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_NAME)

        mainWidget = QWidget(self)
        self.setWidget(mainWidget)
        mainWidget.setLayout(QVBoxLayout())

        previousBrushButton = self.create_button("Previous Brush", mainWidget, self.previous_brush)
        mainWidget.layout().addWidget(previousBrushButton)

        undoButton = self.create_button("Undo", mainWidget, self.undo)
        mainWidget.layout().addWidget(undoButton)

        rotateContainer = QWidget(self)
        rotateContainer.setLayout(QHBoxLayout())

        mainWidget.layout().addWidget(rotateContainer)
        rotateLeftButton = self.create_button("L", rotateContainer,  self.rotate_left)
        rotateRightButton = self.create_button("R", rotateContainer,  self.rotate_right)
        rotateContainer.layout().addWidget(rotateLeftButton)
        rotateContainer.layout().addWidget(rotateRightButton)

        redoButton = self.create_button("Redo", mainWidget, self.redo)
        mainWidget.layout().addWidget(redoButton)


        resetCanvasContainer = QWidget(self)
        resetCanvasContainer.setLayout(QHBoxLayout())
        mainWidget.layout().addWidget(resetCanvasContainer)


        resetZoomButton = self.create_button("100%", mainWidget, self.reset_zoom)
        resetCanvasContainer.layout().addWidget(resetZoomButton)
        resetCanvasRotationButton = self.create_button("Reset", mainWidget, self.reset_canvas_rotation)
        resetCanvasContainer.layout().addWidget(resetCanvasRotationButton)


        canvasContainer = QWidget(self)
        canvasContainer.setLayout(QHBoxLayout())
        mainWidget.layout().addWidget(canvasContainer)
        mirrorCanvasButton = self.create_button("Mirror", canvasContainer, self.mirror_canvas)
        canvasContainer.layout().addWidget(mirrorCanvasButton)
        onlyCanvasButton = self.create_button("Only", canvasContainer, self.only_canvas)
        canvasContainer.layout().addWidget(onlyCanvasButton)




    def canvasChanged(self, canvas):
        pass


instance = Krita.instance()
dock_widget_factory = DockWidgetFactory(DOCKER_ID,
                                                DockWidgetFactoryBase.DockLeft,
                                                HenriksOnscreenKritaShortcutButtons)

instance.addDockWidgetFactory(dock_widget_factory)
