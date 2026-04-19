import { ChangeDetectionStrategy, Component, computed, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ChatMessage } from './models/chat_message.model';
import { getAllChat } from './models/chat_seed';
import { DatePipe } from '@angular/common';
import { ApiService } from './services/api-services';
import { rxResource, toObservable, toSignal } from '@angular/core/rxjs-interop';
import { startWith, switchMap } from 'rxjs';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormsModule, DatePipe],
  templateUrl: './app.html',
  styleUrl: './app.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class App {
  private readonly apiService = inject(ApiService);
  // form fields
  name = signal('');
  message = signal('');

  reloadKey = signal(0);

  // chats = signal<ChatMessage[]>(getAllChat());
  chatsResource = rxResource({
    params: () => ({
      reloadKey: this.reloadKey(),
    }),
    stream: () => this.apiService.getAllChat(),
    defaultValue: [] as ChatMessage[],
  });

  chats = computed(() => this.chatsResource.value());
  isLoading = computed(() => this.chatsResource.isLoading());
  error = computed(() => this.chatsResource.error());

  isFormInvalid = computed(() => {
    return !this.name().trim() || !this.message().trim();
  });

  protected onSendMessage(): void {
    const payload = {
      name: this.name().trim(),
      message: this.message().trim(),
    };

    if (!payload.name || !payload.message) return;

    this.apiService.sendMessage(payload).subscribe({
      next: () => {
        this.name.set('');
        this.message.set('');
        this.reloadKey.update((value) => value + 1);
      },
      error: (error) => {
        console.error('Error while sending message:', error);
      },
    });
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
