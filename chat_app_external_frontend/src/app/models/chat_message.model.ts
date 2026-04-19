export interface ChatMessage {
  name: string;
  message: string;
  created_at: string;
}

export interface ChatApiItem {
  model: string;
  pk: number;
  fields: {
    name: string;
    message: string;
    created_at: string;
  };
}
