import { describe, it, expect } from 'vitest';
import { TitanAI, process } from '../src/index';

describe('TitanAI', () => {
  it('should create instance with default version', () => {
    const sdk = new TitanAI();
    expect(sdk.getVersion()).toBe('0.1.0');
  });

  it('should process data', () => {
    const sdk = new TitanAI();
    const result = sdk.process({ name: 'TitanAI' });
    expect(result).toBe('{"name":"TitanAI"}');
  });

  it('should use process utility', () => {
    const result = process([1, 2, 3]);
    expect(result).toBe('[1,2,3]');
  });
});
