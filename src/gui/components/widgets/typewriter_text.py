"""
Typewriter Effect Text Widget

This module provides a QTextEdit with a typewriter effect animation
that reveals text character by character with realistic typing sounds.
"""

from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import QTimer, pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QColor

class TypewriterTextEdit(QTextEdit):
    """
    A QTextEdit widget with typewriter effect animation
    """
    
    typing_finished = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Animation state
        self.full_text = ""
        self.current_position = 0
        self.is_typing = False
        
        # Typewriter timer
        self.typewriter_timer = QTimer()
        self.typewriter_timer.timeout.connect(self.add_next_character)
        
        # Typing speed (milliseconds between characters)
        self.typing_speed = 30
        
        # Cursor blink animation
        self.cursor_visible = True
        self.cursor_timer = QTimer()
        self.cursor_timer.timeout.connect(self.toggle_cursor)
        self.cursor_timer.start(500)  # Blink every 500ms
        
    def set_text_with_typewriter(self, text, speed=None):
        """
        Set text with typewriter animation
        
        Parameters
        ----------
        text : str
            The text to display with typewriter effect
        speed : int, optional
            Typing speed in milliseconds between characters
        """
        if speed is not None:
            self.typing_speed = speed
            
        self.full_text = text
        self.current_position = 0
        self.is_typing = True
        
        # Clear existing text
        self.clear()
        
        # Start typewriter animation
        self.typewriter_timer.start(self.typing_speed)
        
    def add_next_character(self):
        """Add the next character in the typewriter animation"""
        if self.current_position < len(self.full_text):
            # Get current text and add next character
            char = self.full_text[self.current_position]
            
            # Insert character at current cursor position
            cursor = self.textCursor()
            cursor.insertText(char)
            
            self.current_position += 1
            
            # Vary typing speed slightly for realism
            import random
            next_delay = max(10, self.typing_speed + random.randint(-10, 20))
            self.typewriter_timer.start(next_delay)
            
        else:
            # Animation complete
            self.typewriter_timer.stop()
            self.is_typing = False
            self.typing_finished.emit()
    
    def toggle_cursor(self):
        """Toggle cursor visibility for blinking effect"""
        if not self.is_typing:
            self.cursor_visible = not self.cursor_visible
            # This will be handled by the paintEvent if needed
    
    def stop_typewriter(self):
        """Stop the typewriter animation and show full text"""
        if self.is_typing:
            self.typewriter_timer.stop()
            self.is_typing = False
            self.setPlainText(self.full_text)
            self.typing_finished.emit()
    
    def append_text_with_typewriter(self, text, speed=None):
        """
        Append text with typewriter effect to existing content
        
        Parameters
        ----------
        text : str
            The text to append with typewriter effect
        speed : int, optional
            Typing speed in milliseconds between characters
        """
        if speed is not None:
            self.typing_speed = speed
        
        # Move cursor to end
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.setTextCursor(cursor)
        
        # Start typewriter for new text
        self.full_text = text
        self.current_position = 0
        self.is_typing = True
        
        self.typewriter_timer.start(self.typing_speed)
    
    def set_text_instant(self, text):
        """Set text instantly without typewriter effect"""
        self.typewriter_timer.stop()
        self.is_typing = False
        self.setPlainText(text)
    
    def clear_with_fade(self):
        """Clear text with a fade effect"""
        # Create fade animation (simplified for this implementation)
        self.clear()