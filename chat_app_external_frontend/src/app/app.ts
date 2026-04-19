import { ChangeDetectionStrategy, Component, computed, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ChatMessage } from './models/chat_message.model';
import { getAllChat } from './models/chat_seed';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormsModule, DatePipe],
  templateUrl: './app.html',
  styleUrl: './app.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class App {
  // form fields
  name = signal('');
  message = signal('');

  chats = signal<ChatMessage[]>(getAllChat());

  isFormInvalid = computed(() => {
    return !this.name().trim() || !this.message().trim();
  });

  protected sendMessage(): void {
    if (this.isFormInvalid()) return;

    const newMessage: ChatMessage = {
      name: this.name().trim(),
      message: this.message().trim(),
      created_at: new Date().toISOString().slice(0, 10),
    };

    this.chats.update((current) => [...current, newMessage]);
    this.name.set('');
    this.message.set('');
  }

  protected getAvatarStyle(name: string): { [key: string]: string } {
    const hue = this.stringToHue(name);
    return {
      background: `linear-gradient(135deg, hsl(${hue} 85% 55%), hsl(${(hue + 35) % 360} 85% 45%))`,
      color: 'white',
    };
  }

  protected getNameStyle(name: string): { [key: string]: string } {
    const hue = this.stringToHue(name);
    return {
      color: `hsl(${hue} 70% 40%)`,
    };
  }

  private stringToHue(value: string): number {
    let hash = 0;
    for (let i = 0; i < value.length; i++) {
      hash = value.charCodeAt(i) + ((hash << 5) - hash);
    }
    return Math.abs(hash) % 360;
  }
}
