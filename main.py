import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from core.game_state import GameState
from core.epidemic_engine import EpidemicEngine

class BasicMainWindow(QMainWindow):
    def __init__(self, state: GameState):
        super().__init__()
        self.state = state
        self.setWindowTitle("Pandemic Command - Pre-Alpha M0")
        self.resize(400, 200)

        # UI Components
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.info_label = QLabel(self._get_state_text())
        self.layout.addWidget(self.info_label)

        self.next_turn_btn = QPushButton("Next Turn (1 Week)")
        self.next_turn_btn.clicked.connect(self.handle_next_turn)
        self.layout.addWidget(self.next_turn_btn)

    def _get_state_text(self) -> str:
        return (f"Date: {self.state.current_date.strftime('%d-%m-%Y')} (Turn {self.state.turn})\n"
                f"Infectious: {self.state.infectious}\n"
                f"Budget: ${self.state.budget_mil_usd}M\n"
                f"Satisfaction: {self.state.satisfaction_index}%")
    
    def handle_next_turn(self):
        self.engine.simulate_one_week()
        self.state.advance_turn()
        self.info_label.setText(self._get_state_text()) # Update UI

if __name__ == "__main__":
    app = QApplication(sys.argv)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    theme_path = os.path.join(current_dir, "ui", "styles", "dark_theme.qss")

    try:
        with open(theme_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print(f"WARNING: Can not find theme file at {theme_path}")
    # Init model
    initial_state = GameState()

    # Init View
    window = BasicMainWindow(initial_state)
    window.engine = EpidemicEngine(initial_state)
    window.show()

    sys.exit(app.exec())