import EmojiPicker, {
  Emoji,
  EmojiStyle,
  Theme as EmojiTheme,
} from "emoji-picker-react";

import { ModelType } from "../store";

import BotIconOpenAI from "../icons/llm-icons/openai.svg";
import BotIconGemini from "../icons/llm-icons/gemini.svg";
import BotIconGemma from "../icons/llm-icons/gemma.svg";
import BotIconClaude from "../icons/llm-icons/claude.svg";
import BotIconMeta from "../icons/llm-icons/meta.svg";
import BotIconMistral from "../icons/llm-icons/mistral.svg";
import BotIconDeepseek from "../icons/llm-icons/deepseek.svg";
import BotIconMoonshot from "../icons/llm-icons/moonshot.svg";
import BotIconQwen from "../icons/llm-icons/qwen.svg";
import BotIconWenxin from "../icons/llm-icons/wenxin.svg";
import BotIconGrok from "../icons/llm-icons/grok.svg";
import BotIconHunyuan from "../icons/llm-icons/hunyuan.svg";
import BotIconDoubao from "../icons/llm-icons/doubao.svg";
import BotIconChatglm from "../icons/llm-icons/chatglm.svg";

export function getEmojiUrl(unified: string, style: EmojiStyle) {
  // Whoever owns this Content Delivery Network (CDN), I am using your CDN to serve emojis
  // Old CDN broken, so I had to switch to this one
  // Author: https://github.com/H0llyW00dzZ
  return `https://fastly.jsdelivr.net/npm/emoji-datasource-apple/img/${style}/64/${unified}.png`;
}

export function AvatarPicker(props: {
  onEmojiClick: (emojiId: string) => void;
}) {
  return (
    <EmojiPicker
      width={"100%"}
      lazyLoadEmojis
      theme={EmojiTheme.AUTO}
      getEmojiUrl={getEmojiUrl}
      onEmojiClick={(e) => {
        props.onEmojiClick(e.unified);
      }}
    />
  );
}

export function Avatar(props: { model?: ModelType; avatar?: string }) {
  if (props.model) {
    const modelName = props.model.toLowerCase();

    if (
      modelName.startsWith("gpt") ||
      modelName.startsWith("chatgpt") ||
      modelName.startsWith("dall-e") ||
      modelName.startsWith("dalle") ||
      modelName.startsWith("o1") ||
      modelName.startsWith("o3")
    ) {
      return (
        <div className="no-dark">
          <BotIconOpenAI className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("gemini")) {
      return (
        <div className="no-dark">
          <BotIconGemini className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("gemma")) {
      return (
        <div className="no-dark">
          <BotIconGemma className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("claude")) {
      return (
        <div className="no-dark">
          <BotIconClaude className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.includes("llama")) {
      return (
        <div className="no-dark">
          <BotIconMeta className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("mixtral") || modelName.startsWith("codestral")) {
      return (
        <div className="no-dark">
          <BotIconMistral className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.includes("deepseek")) {
      return (
        <div className="no-dark">
          <BotIconDeepseek className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("moonshot")) {
      return (
        <div className="no-dark">
          <BotIconMoonshot className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("qwen")) {
      return (
        <div className="no-dark">
          <BotIconQwen className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("ernie")) {
      return (
        <div className="no-dark">
          <BotIconWenxin className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("grok")) {
      return (
        <div className="no-dark">
          <BotIconGrok className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("hunyuan")) {
      return (
        <div className="no-dark">
          <BotIconHunyuan className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (modelName.startsWith("doubao") || modelName.startsWith("ep-")) {
      return (
        <div className="no-dark">
          <BotIconDoubao className="user-avatar" width={30} height={30} />
        </div>
      );
    } else if (
      modelName.includes("glm") ||
      modelName.startsWith("cogview-") ||
      modelName.startsWith("cogvideox-")
    ) {
      return (
        <div className="no-dark">
          <BotIconChatglm className="user-avatar" width={30} height={30} />
        </div>
      );
    }

    return (
      <div className="no-dark">
        <img src="/titan.jpg" className="user-avatar" width={30} height={30} style={{ borderRadius: "50%", objectFit: "cover" }} />
      </div>
    );
  }

  return (
    <div className="user-avatar">
      {props.avatar && <EmojiAvatar avatar={props.avatar} />}
    </div>
  );
}

export function EmojiAvatar(props: { avatar: string; size?: number }) {
  return (
    <Emoji
      unified={props.avatar}
      size={props.size ?? 18}
      getEmojiUrl={getEmojiUrl}
    />
  );
}
