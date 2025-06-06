"""
Audio Visualizer Widget with Real-time Waveform Animation

This module provides a stunning animated waveform visualization that responds to audio input
with particle effects, neon glows, and smooth animations.
"""

import math
import random
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QTimer, pyqtSignal, QRect
from PyQt6.QtGui import QPainter, QLinearGradient, QColor, QPen, QBrush
from PyQt6.QtCore import Qt

class AudioVisualizer(QWidget):
    """
    Futuristic audio waveform visualizer with particle effects
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(120)
        self.setMinimumWidth(400)
        
        # Animation state
        self.is_recording = False
        self.animation_frame = 0
        self.bars = []
        self.particles = []
        
        # Initialize waveform bars
        self.bar_count = 50
        self.setup_bars()
        
        # Animation timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)  # 20 FPS
        
    def setup_bars(self):
        """Initialize the waveform bars with random heights"""
        self.bars = []
        for i in range(self.bar_count):
            self.bars.append({
                'height': random.uniform(0.1, 0.3),
                'target_height': random.uniform(0.1, 0.3),
                'velocity': 0,
                'hue': random.uniform(40, 60)  # Gold range for recording
            })
    
    def start_recording(self):
        """Start the recording animation"""
        self.is_recording = True
        
    def stop_recording(self):
        """Stop the recording animation"""
        self.is_recording = False
        
    def update_animation(self):
        """Update animation frame and bar heights"""
        self.animation_frame += 1
        
        # Update bars
        for i, bar in enumerate(self.bars):
            if self.is_recording:
                # Active animation - dynamic waveform
                # Create wave pattern with some randomness
                wave = math.sin((self.animation_frame + i * 3) * 0.1) * 0.3
                noise = random.uniform(-0.1, 0.1)
                bar['target_height'] = max(0.2, min(1.0, 0.5 + wave + noise))
            else:
                # Idle animation - gentle pulse
                pulse = math.sin((self.animation_frame + i * 2) * 0.05) * 0.1
                bar['target_height'] = max(0.1, 0.2 + pulse)
            
            # Smooth interpolation
            diff = bar['target_height'] - bar['height']
            bar['velocity'] += diff * 0.1
            bar['velocity'] *= 0.8  # Damping
            bar['height'] += bar['velocity']
            
            # Update hue for color cycling
            if self.is_recording:
                bar['hue'] = (bar['hue'] + 0.5) % 360
            else:
                bar['hue'] = (bar['hue'] + 0.1) % 360
        
        # Update particles
        self.update_particles()
        
        self.update()
    
    def update_particles(self):
        """Update particle effects"""
        # Add new particles when recording
        if self.is_recording and random.random() < 0.3:
            self.particles.append({
                'x': random.uniform(0, self.width()),
                'y': self.height() - 20,
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(-5, -1),
                'life': 1.0,
                'size': random.uniform(2, 6),
                'color': QColor.fromHsv(random.randint(40, 60), 200, 255)  # Gold particles
            })
        
        # Update existing particles
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['vy'] += 0.1  # Gravity
            particle['life'] -= 0.02
            
            if particle['life'] <= 0:
                self.particles.remove(particle)
    
    def paintEvent(self, event):
        """Custom paint event for the visualizer"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Background gradient
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(10, 15, 30, 50))
        gradient.setColorAt(1, QColor(20, 30, 60, 80))
        painter.fillRect(self.rect(), QBrush(gradient))
        
        # Draw waveform bars
        bar_width = self.width() / self.bar_count
        
        for i, bar in enumerate(self.bars):
            x = i * bar_width
            height = bar['height'] * (self.height() - 40)
            y = self.height() - height - 20
            
            # Create gradient for each bar
            bar_gradient = QLinearGradient(0, y, 0, y + height)
            
            if self.is_recording:
                # Gold colors when recording
                color1 = QColor(255, 210, 63, 200)  # Gold
                color2 = QColor(255, 180, 0, 100)   # Darker gold
            else:
                # Subtle cyan when idle
                color1 = QColor(0, 217, 255, 150)  # Cyan
                color2 = QColor(0, 150, 200, 80)   # Darker cyan
            
            bar_gradient.setColorAt(0, color1)
            bar_gradient.setColorAt(1, color2)
            
            # Draw bar with glow effect
            painter.setBrush(QBrush(bar_gradient))
            painter.setPen(Qt.PenStyle.NoPen)
            
            # Main bar
            bar_rect = QRect(int(x + 1), int(y), int(bar_width - 2), int(height))
            painter.drawRoundedRect(bar_rect, 2, 2)
            
            # Glow effect when recording
            if self.is_recording and bar['height'] > 0.5:
                glow_pen = QPen(color1, 2)
                painter.setPen(glow_pen)
                painter.setBrush(Qt.BrushStyle.NoBrush)
                glow_rect = QRect(int(x), int(y - 2), int(bar_width), int(height + 4))
                painter.drawRoundedRect(glow_rect, 4, 4)
        
        # Draw particles
        for particle in self.particles:
            alpha = int(particle['life'] * 255)
            color = QColor(particle['color'])
            color.setAlpha(alpha)
            
            painter.setBrush(QBrush(color))
            painter.setPen(Qt.PenStyle.NoPen)
            
            size = particle['size'] * particle['life']
            painter.drawEllipse(
                int(particle['x'] - size/2), 
                int(particle['y'] - size/2), 
                int(size), 
                int(size)
            )
        
        # Draw center frequency line when recording
        if self.is_recording:
            center_y = self.height() // 2
            line_gradient = QLinearGradient(0, center_y, self.width(), center_y)
            line_gradient.setColorAt(0, QColor(255, 210, 63, 0))
            line_gradient.setColorAt(0.5, QColor(255, 210, 63, 100))
            line_gradient.setColorAt(1, QColor(255, 210, 63, 0))
            
            painter.setPen(QPen(QBrush(line_gradient), 2))
            painter.drawLine(0, center_y, self.width(), center_y)