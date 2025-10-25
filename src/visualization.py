import matplotlib.pyplot as plt
import seaborn as sns

def plot_approval_vs_delay(df, save_path):
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x='approval_time_days', y='delay_days', alpha=0.7)
    plt.title('Approval Time vs Delay Days')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
