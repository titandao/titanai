export interface TitanAIConfig {
  version: string;
}

export class TitanAI {
  private version: string;

  constructor(config?: Partial<TitanAIConfig>) {
    this.version = config?.version || '0.1.0';
  }

  process<T>(data: T): string {
    return JSON.stringify(data);
  }

  getVersion(): string {
    return this.version;
  }
}

export function process<T>(data: T): string {
  const sdk = new TitanAI();
  return sdk.process(data);
}

export default TitanAI;
