from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

# 示例站点与关键词，仅用于展示数据
SITE_URL = "https://official-cn-i-game.com.cn"
KEYWORD = "爱游戏"


@dataclass
class KeywordNote:
    """表示一条关键词笔记的数据类"""
    note_id: int
    keyword: str
    content: str
    source_url: str
    tags: List[str] = field(default_factory=list)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = self.created_at

    def summary(self, max_length: int = 60) -> str:
        """返回笔记内容的简短摘要"""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length].rstrip() + "…"

    def tag_string(self, separator: str = ", ") -> str:
        """返回以分隔符连接的标签字符串"""
        return separator.join(self.tags) if self.tags else "（无标签）"


def format_single_note(note: KeywordNote, show_id: bool = False) -> str:
    """格式化输出单条笔记，返回多行文本"""
    lines = []
    if show_id:
        lines.append(f"[{note.note_id}] 关键词：{note.keyword}")
    else:
        lines.append(f"关键词：{note.keyword}")
    lines.append(f"来源：{note.source_url}")
    lines.append(f"标签：{note.tag_string()}")
    lines.append(f"创建时间：{note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"更新时间：{note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"内容：{note.content}")
    return "\n".join(lines)


def format_note_list(notes: List[KeywordNote], max_summary: int = 80) -> str:
    """格式化输出多条笔记的列表摘要"""
    if not notes:
        return "（暂无笔记）"
    result_parts = []
    for note in notes:
        summary_text = note.summary(max_summary)
        result_parts.append(
            f"• {note.keyword} | {note.source_url} | {summary_text}"
        )
    return "\n".join(result_parts)


def build_example_notes() -> List[KeywordNote]:
    """构造一组示例笔记，包含核心关键词与URL"""
    return [
        KeywordNote(
            note_id=1,
            keyword=KEYWORD,
            content="爱游戏平台提供了丰富的游戏资源和社区互动功能，用户可以在这里找到各类热门游戏。",
            source_url=SITE_URL,
            tags=["游戏", "社区", "资源"],
            created_at=datetime(2024, 3, 10, 14, 30),
        ),
        KeywordNote(
            note_id=2,
            keyword=KEYWORD,
            content="爱游戏近期推出了全新版本，优化了界面交互和性能体验，吸引大量新用户注册。",
            source_url=SITE_URL + "/news",
            tags=["更新", "版本", "优化"],
            created_at=datetime(2024, 5, 22, 9, 15),
        ),
        KeywordNote(
            note_id=3,
            keyword=KEYWORD,
            content="爱游戏官方公告：将于下月举办线上电竞赛事，报名通道现已开放。",
            source_url=SITE_URL + "/events",
            tags=["活动", "赛事", "公告"],
            created_at=datetime(2024, 7, 1, 10, 0),
        ),
    ]


def main():
    """主运行函数：展示示例笔记的格式化输出"""
    notes = build_example_notes()
    print("=== 单条笔记详细格式 ===")
    print(format_single_note(notes[0], show_id=True))
    print()
    print("=== 笔记列表摘要 ===")
    print(format_note_list(notes))
    print()
    print("=== 所有笔记的简短摘要 ===")
    for note in notes:
        print(f"  ID {note.note_id}: {note.summary(40)}")
    print()
    print(f"示例配置：站点={SITE_URL}，核心关键词={KEYWORD}")


if __name__ == "__main__":
    main()