# BU RISE 2026: Understanding Reasoning Capability Loss in Knowledge Distillation

Overview/Project Details:
-

**Core Research Question** 

When a smaller "student" model is distilled from a larger "teacher" model, what specific reasoning capabilities or information degrade, disappear, or get reshaped — and can we characterize where and why this happens, rather than just measuring an aggregate benchmark drop?


**Guiding Hypothesis**

Distillation loss isn't uniform. It likely impacts long-tail knowledge and certain tasks more instead of degrading everything proportionally. The project aims to produce a capability-loss profile, not just a single number.

**Link to Poster**: https://canva.link/69hlumn8sxv9bf8

Abstract
-

**Mind the Gap: Determining Where Capability Loss Occurs in Distilled Vision-Language Models**

Preksha Shyamsukha, Siwoo Song, Xavier Thomas, Dahye Kim, Deepti Ghadiyaram

American High School, 36300 Fremont Blvd, Fremont, CA 94536, William A. Shine Great Neck South High School, 341 Lakeville Rd, Lake Success, NY 11020, Boston University, Commonwealth Ave, Boston, MA 022153

Knowledge distillation (KD) is the process of fine-tuning a lightweight student model on the probability distribution of a larger teacher model, with the goal of the student performing on par with the teacher. It has been observed that distillation often causes a degradation of reasoning capabilities, primarily measured by aggregate benchmark scores. However, this metric fails to capture how capability loss occurs disproportionately across different categories in the benchmark. Our research aims to develop a comprehensive capability-loss profile on the InternVL2-8B (teacher), InternVL2-2B (baseline student), and TAID-VLM-2B (InternVL2-2B KD student) models to determine what specific tasks are impacted by the capability loss. We compare performance differences between the teacher and student models across multiple benchmarks (MME, HallusionBench, JailBreakV, etc.) with both default and varied generation parameters (e.g. temperature, top_k, etc.). We observe that the models are sensitive to changes in temperature and top_k for certain categories, but overall performance differences remain similar. The KD student typically performs better than the baseline student but worse than the teacher. Notably, on safety-related tasks, we observe that the KD student’s performance is much closer to that of the baseline student rather than that of the teacher, demonstrating that distillation did not effectively transfer the teacher’s safety critical capabilities to the student. The differences were larger for more nuanced scenarios (e.g. political lobbying, economic harm) and smaller for clear-cut scenarios (e.g. hate speech). Both student models consistently outperform the teacher on several fine-grained recognition tasks (e.g. distinguishing scenes) and underperform on several mathematical tasks. These results confirm that the capability loss between teacher and student is nonuniform. We further investigate the causes of this capability loss by training probing linear classifiers on hidden layers of these models to determine whether the culprit is the capacity limit or distillation, potentially highlighting critical gaps in the distillation process.
