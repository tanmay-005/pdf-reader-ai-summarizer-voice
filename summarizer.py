from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1


summarizer = pipeline(
    "summarization",
    model = "facebook/bart-large-cnn",
    device = device
)

def summarize_chunk(text, max_length=200, min_length=30):
    result = summarizer(text,
                        max_length=max_length,
                        min_length=min_length,
                        do_sample=False)
    return result[0]["summary_text"]

if __name__ == "__main__":
    sample_text = """Technology has become an inseparable part of modern life, influencing the way people communicate, work, learn, travel, and entertain themselves. A few decades ago, many activities that are now completed within seconds required significant amounts of time and effort. People depended heavily on physical documents, landline telephones, libraries, and face-to-face meetings. Today, smartphones, computers, and the internet allow individuals to access information and communicate with others from almost anywhere in the world. This rapid development has created many opportunities, but it has also introduced new challenges that society must learn to manage responsibly.

One of the most noticeable effects of technology can be seen in education. Students can now attend online classes, watch educational videos, read digital books, and access research papers without visiting a library. Online learning platforms allow people to study subjects at their own pace and revisit difficult concepts whenever necessary. Artificial intelligence has also become increasingly useful in education by helping students understand complicated topics, generate practice questions, organize information, and receive immediate feedback. However, technology should not completely replace traditional learning. Students still need critical thinking, communication skills, creativity, and the ability to work with other people.

Technology has also transformed the workplace. Many companies now allow employees to work remotely, communicate through video conferences, and collaborate on documents in real time. Automation has reduced the need for people to perform repetitive tasks, allowing them to focus on activities that require creativity and decision-making. At the same time, automation has created concerns about employment because some traditional jobs may disappear as machines become more capable. This means that workers increasingly need to learn new skills and adapt to changing industries.

Despite its advantages, technology can create problems when it is used without limits. Spending too much time on social media or digital entertainment can reduce physical activity and interfere with concentration. Constant notifications can make it difficult for people to focus on important tasks. Privacy is another major concern because many online services collect information about their users. People therefore need to understand how their data is collected, stored, and shared.

The future of technology will likely bring even greater changes. Artificial intelligence, robotics, renewable energy, biotechnology, and advanced computing could transform many areas of society. However, technological progress should be guided by ethical considerations. New inventions should improve people's lives without unnecessarily harming individuals, communities, or the environment. Ultimately, technology is neither completely good nor completely bad. Its impact depends largely on how people design, regulate, and use it. The most successful societies will be those that embrace innovation while maintaining responsibility, human judgment, and concern for the well-being of others."""

    print(summarize_chunk(sample_text))